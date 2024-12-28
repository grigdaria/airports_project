from config import SUPABASE_URL,SUPABASE_KEY
from supabase import create_client, Client

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_airports():
    # Выполнение POST-запроса к функции get_all_airports
    response = supabase.rpc('get_all_airports').execute()

    # Возвращаем данные
    return response.data

def get_all_coastline():
    # Выполнение POST-запроса к функции get_all_airports
    response = supabase.rpc('get_all_coastline').execute()

    # Возвращаем данные
    return response.data

print(get_all_airports())

