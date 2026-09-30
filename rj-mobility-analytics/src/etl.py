import json
import pandas as pd
from datetime import datetime
from src.database import SessionLocal, engine, Base
from src.models import VeiculoModel, PosicaoGPSModel

def extrair_dados_mobilidade():
    """
    Carrega os dados de telemetria a partir do cache local JSON estruturado.
    """
    print("A carregar dados a partir do cache local...")
    caminho_cache = "src/cache_sppo.json"
    
    try:
        with open(caminho_cache, "r", encoding="utf-8") as f:
            dados = json.load(f)
            total = len(dados.get('veiculos', []))
            print(f"Sucesso! {total} registos carregados do cache local.")
            return dados
    except Exception as e:
        print(f"Erro ao ler o arquivo de cache: {e}")
        return None

def transformar_e_carregar(dados_brutos):
    """
    Garante a criação das tabelas, trata os dados com Pandas e persiste no PostgreSQL.
    """
    if not dados_brutos or 'veiculos' not in dados_brutos:
        print("Estrutura de dados inválida ou vazia.")
        return

    # Garante que as tabelas existem no banco de dados antes de inserir
    print("A verificar e criar tabelas no PostgreSQL se necessário...")
    Base.metadata.create_all(bind=engine)

    df = pd.DataFrame(dados_brutos['veiculos'])
    
    colunas_necessarias = ['ordem', 'latitude', 'longitude']
    if not all(col in df.columns for col in colunas_necessarias):
        print("O cache não contém as colunas esperadas.")
        return

    df = df.dropna(subset=colunas_necessarias)
    
    session = SessionLocal()
    try:
        print("Iniciando carga dos dados no PostgreSQL...")
        inseridos = 0
        
        for _, row in df.iterrows():
            ordem_veiculo = str(row['ordem'])
            linha_veiculo = str(row.get('linha', 'N/D'))
            
            # Verifica ou cadastra o veículo
            veiculo = session.query(VeiculoModel).filter_by(ordem=ordem_veiculo).first()
            if not veiculo:
                veiculo = VeiculoModel(ordem=ordem_veiculo, linha=linha_veiculo)
                session.add(veiculo)
                session.commit()
                session.refresh(veiculo)

            # Insere a telemetria GPS vinculada ao veículo
            nova_posicao = PosicaoGPSModel(
                veiculo_id=veiculo.id,
                latitude=float(row['latitude']),
                longitude=float(row['longitude']),
                velocidade=float(row.get('velocidade', 0.0)),
                datahora_servidor=datetime.now()
            )
            session.add(nova_posicao)
            inseridos += 1
        
        session.commit()
        print(f"Carga concluída com sucesso! {inseridos} posições de GPS salvas no banco.")
        
    except Exception as e:
        session.rollback()
        print(f"Erro durante a carga no banco: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    dados = extrair_dados_mobilidade()
    if dados:
        transformar_e_carregar(dados)