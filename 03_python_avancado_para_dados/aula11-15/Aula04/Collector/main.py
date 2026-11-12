import sys
from pathlib import Path

# Adiciona o diretório do Collector ao sys.path para permitir importações dos módulos locais
sys.path.append(str(Path(__file__).parent))

from datasource.api import APICollector
from contracts.schema import CompraSchema
from tools.aws.client import S3Client

import time
import schedule

schema = CompraSchema
supabase = S3Client()


def apiCollector(schema, supabase, repeat):
    response = APICollector(schema, supabase).start(repeat)
    print('Executei')
    return

schedule.every(1).minutes.do(apiCollector,schema, supabase, 2)

# Executa imediatamente a primeira vez para testar:
apiCollector(schema, supabase, 2)

while True:
    schedule.run_pending()
    time.sleep(1)
