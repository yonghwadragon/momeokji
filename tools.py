# tools.py
import pandas as pd
import os
import random

file_path = 'Cooking.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"'{file_path}' 파일이 없습니다. 경로: {os.getcwd()}")

try:
    CK = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    CK = pd.read_csv(file_path, encoding='euc-kr')

CK['NEW_COL'] = CK[['INQ_CNT', 'RCMM_CNT', 'SRAP_CNT']].sum(axis=1) / 3
selected_CK = CK.iloc[:, [2, 13]]
CK_cl = selected_CK.dropna()
final_data = CK_cl.drop_duplicates(subset='CKG_NM')

def find_recipe_with_ingredients(ingredients):
    """
    사용자 입력 재료(ingredients)를 모두 부분 일치로 포함하는 레시피 중 하나를 무작위 선택
    예) ingredients=["양파","감자"]
    """
    def cook(selected_ings):
        recipes = []
        for _, row in final_data.iterrows():
            recipe_ingredients = str(row['CKG_MTRL_CN']).lower()
            # 부분 일치: 각 ing이 recipe_ingredients 내에 있으면 OK
            if all(ing in recipe_ingredients for ing in selected_ings):
                recipes.append(row['CKG_NM'])
        return recipes

    selected_ingredients = [ing.strip().lower() for ing in ingredients]
    dishes = cook(selected_ingredients)

    if not dishes:
        return "적합한 요리를 찾을 수 없습니다."

    dish = random.choice(dishes)
    dish_row = final_data[final_data['CKG_NM'] == dish]
    dish_ingredients = dish_row['CKG_MTRL_CN'].values[0]
    return f"'{dish}' 추천할게요! 재료: {dish_ingredients}"