from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/index_p',methods=['GET', 'POST'])
def index_p():
    return render_template('index_p.html')

@app.route('/result', methods=['POST'])
def result():
    global yourType
    years = request.form.get('years')
    months = request.form.get('months')
    days = request.form.get('days')
    # return render_template('result.html')

    years = int(years)
    df = pd.read_csv(f'data/{years}.csv')
    days = int(days)
    months = int(months)
    meisu = df.iloc[days - 1, months]
    meisu = meisu.replace('-', '')

    current = datetime.now()
    current_year = current.year
    current_year = int(current_year)

    if (years % 2) == 0:
        even_odd = '金'
    else:
        even_odd = '銀'
    years = int(years)
    age = current_year - years
    # global yourType
    # 壮年期（命数３を採用）
    if age > 60:
        if meisu[0:2] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[0:2]}'

        elif meisu[0:2] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[0:2]}'

        elif meisu[0:2] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[0:2]}'

        elif meisu[0:2] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[0:2]}'

        elif meisu[0:2] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[0:2]}'

        elif meisu[0:2] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[0:2]}'
        else:
            print('その他')


    # 青年期（命数２を採用）
    elif age > 30:
        if meisu[2:4] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[2:4]}'

        elif meisu[2:4] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[2:4]}'

        elif meisu[2:4] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[2:4]}'

        elif meisu[2:4] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[2:4]}'

        elif meisu[2:4] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[2:4]}'

        elif meisu[2:4] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[2:4]}'
        else:
            print('その他')

    # 幼年期（命数１を採用）
    elif age > 0:
        if meisu[4:6] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[4:6]}'

        elif meisu[4:6] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[4:6]}'

        elif meisu[4:6] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[4:6]}'

        elif meisu[4:6] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[4:6]}'

        elif meisu[4:6] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[4:6]}'

        elif meisu[4:6] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[4:6]}'
        else:
            print('その他')
    else:
        pass


    # 羅針盤
    if yourType == '金の羅針盤01':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()


    elif yourType == '金の羅針盤02':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()



    elif yourType == '金の羅針盤03':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()




    elif yourType == '金の羅針盤04':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()


    elif yourType == '金の羅針盤05':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の羅針盤06':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の羅針盤07':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の羅針盤08':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の羅針盤09':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の羅針盤10':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤01':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤02':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤03':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤04':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤05':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤06':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤07':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤08':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤09':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の羅針盤10':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()


    # 　インディアン
    elif yourType == '金のインディアン11':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン12':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン13':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン14':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン15':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン16':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン17':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン18':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン19':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のインディアン20':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()


    elif yourType == '銀のインディアン11':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン12':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン13':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン14':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン15':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン16':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン17':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン18':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン19':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のインディアン20':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    # 　鳳凰
    elif yourType == '金の鳳凰21':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰22':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰23':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰24':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰25':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰26':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰27':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰28':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰29':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の鳳凰30':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰21':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰22':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰23':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰24':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰25':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰26':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰27':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰28':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰29':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の鳳凰30':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()


    # 　時計
    elif yourType == '金の時計31':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計32':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計33':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計34':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計35':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計36':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計37':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計38':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計39':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金の時計40':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計31':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計32':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計33':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計34':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計35':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計36':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計37':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計38':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計39':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀の時計40':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    # カメレオン
    elif yourType == '金のカメレオン41':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン42':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン43':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン44':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン45':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン46':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン47':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン48':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン49':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のカメレオン50':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン41':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン42':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン43':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン44':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン45':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン46':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン47':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン48':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン49':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のカメレオン50':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    # イルカ
    elif yourType == '金のイルカ51':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ52':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ53':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ54':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ55':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ56':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ57':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ58':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ59':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '金のイルカ60':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ51':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ52':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ53':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ54':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ55':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ56':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ57':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ58':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ59':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()

    elif yourType == '銀のイルカ60':
        img_path = f'static/img/{yourType[0:-2]}'
        with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
            kekka = f.read()
        with open(f'star/{yourType}.txt', 'r', encoding='utf-8') as f:
            star = f.read()
        with open(f'sex/{yourType}.txt', 'r', encoding='utf-8') as f:
            malefemale = f.read()
        with open(f'backside/{yourType}.txt', 'r', encoding='utf-8') as f:
            backside = f.read()
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    else:
        pass


    return render_template('result.html',
                           age=age,
                           yourType=yourType[0:-2],
                           kekka=kekka,
                           star=star,
                           sex = malefemale,
                           backside = backside,
                           picture = img_path,
                           unsei2022 = unsei2022)


#パートナー診断
@app.route('/partner', methods=['POST'])
def partner():
    global yourType
    years = request.form.get('years')
    months = request.form.get('months')
    days = request.form.get('days')
    # return render_template('result.html')

    years = int(years)
    df = pd.read_csv(f'data/{years}.csv')
    days = int(days)
    months = int(months)
    meisu = df.iloc[days - 1, months]
    meisu = meisu.replace('-', '')

    current = datetime.now()
    current_year = current.year
    current_year = int(current_year)

    if (years % 2) == 0:
        even_odd = '金'
    else:
        even_odd = '銀'
    years = int(years)
    age = current_year - years
    # global yourType
    # 壮年期（命数３を採用）
    if age > 60:
        if meisu[0:2] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[0:2] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[0:2] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[0:2] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[0:2] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[0:2] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[0:2]}'
            img_path = f'static/images/{yourType[0:-2]}'
        else:
            print('その他')


    # 青年期（命数２を採用）
    elif age > 30:
        if meisu[2:4] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[2:4] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[2:4] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[2:4] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[2:4] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[2:4] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[2:4]}'
            img_path = f'static/images/{yourType[0:-2]}'
        else:
            print('その他')

    # 幼年期（命数１を採用）
    elif age > 0:
        if meisu[4:6] < '11':
            print(f'あなたは{even_odd}の羅針盤タイプです。')
            yourType = f'{even_odd}の羅針盤{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[4:6] < '21':
            print(f'あなたは{even_odd}のインディアンタイプです')
            yourType = f'{even_odd}のインディアン{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[4:6] < '31':
            print(f'あなたは{even_odd}の鳳凰タイプです')
            yourType = f'{even_odd}の鳳凰{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[4:6] < '41':
            print(f'あなたは{even_odd}の時計タイプです')
            yourType = f'{even_odd}の時計{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[4:6] < '51':
            print(f'あなたは{even_odd}のカメレオンタイプです')
            yourType = f'{even_odd}のカメレオン{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'

        elif meisu[4:6] < '61':
            print(f'あなたは{even_odd}のイルカタイプです')
            yourType = f'{even_odd}のイルカ{meisu[4:6]}'
            img_path = f'static/images/{yourType[0:-2]}'
        else:
            print('その他')
    else:
        pass

    global p_years
    global p_months
    global p_days
    p_years = request.form.get('p_years')
    p_months = request.form.get('p_months')
    p_days = request.form.get('p_days')
    # パートナーのデータ読み込み

    p_months = int(p_months)
    p_days = int(p_days)
    p_df = pd.read_csv(f'data/{p_years}.csv')
    p_meisu = p_df.iloc[p_days - 1, p_months]
    p_meisu = p_meisu.replace('-', '')
    p_years = int(p_years)
    current = datetime.now()
    current_year = current.year
    current_year = int(current_year)
    if (p_years % 2) == 0:
        p_even_odd = '金'
    else:
        p_even_odd = '銀'
    p_years = int(p_years)
    p_age = current_year - p_years
    global p_yourType
    global p_Type
    # 壮年期（命数３を採用）
    if p_age > 60:
        if p_meisu[0:2] < '11':
            p_yourType = f'{p_even_odd}の羅針盤{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[0:2] < '21':
            p_yourType = f'{p_even_odd}のインディアン{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[0:2] < '31':
            p_yourType = f'{p_even_odd}の鳳凰{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[0:2] < '41':
            p_yourType = f'{p_even_odd}の時計{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[0:2] < '51':
            p_yourType = f'{p_even_odd}のカメレオン{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[0:2] < '61':
            p_yourType = f'{p_even_odd}のイルカ{p_meisu[0:2]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'
        else:
            pass

    # 青年期（命数２を採用）
    elif p_age > 30:
        if p_meisu[2:4] < '11':
            p_yourType = f'{p_even_odd}の羅針盤{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[2:4] < '21':
            p_yourType = f'{p_even_odd}のインディアン{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[2:4] < '31':
            p_yourType = f'{p_even_odd}の鳳凰{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[2:4] < '41':
            p_yourType = f'{p_even_odd}の時計{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[2:4] < '51':
            p_yourType = f'{p_even_odd}のカメレオン{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[2:4] < '61':
            p_yourType = f'{p_even_odd}のイルカ{p_meisu[2:4]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'
        else:
            pass

    # 幼年期（命数１を採用）
    elif p_age > 0:
        if p_meisu[4:6] < '11':
            p_yourType = f'{p_even_odd}の羅針盤{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[4:6] < '21':
            p_yourType = f'{p_even_odd}のインディアン{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[4:6] < '31':
            p_yourType = f'{p_even_odd}の鳳凰{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[4:6] < '41':
            p_yourType = f'{p_even_odd}の時計{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[4:6] < '51':
            p_yourType = f'{p_even_odd}のカメレオン{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'

        elif p_meisu[4:6] < '61':
            p_yourType = f'{p_even_odd}のイルカ{p_meisu[4:6]}'
            p_img_path = f'static/images/{p_yourType[0:-2]}'
        else:
            pass
    else:
        pass

    p_Type = p_yourType[0:-2]


    if yourType[0:-2] == '金の羅針盤':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
                # p_suchi = p_suchi.replace('%', '')

    elif yourType[0:-2] == '銀の羅針盤':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '金のインディアン':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '銀のインディアン':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '金の鳳凰':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '銀の鳳凰':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '金の時計':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()

            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '銀の時計':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '金のカメレオン':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '銀のカメレオン':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '金のイルカ':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    elif yourType[0:-2] == '銀のイルカ':
        if p_Type == '金の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の羅針盤':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のインディアン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の鳳凰':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀の時計':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のカメレオン':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '金のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
        elif p_Type == '銀のイルカ':
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
                p_kekka = f.read()
            with open(f'p_Type/{yourType[0:-2]}/{p_Type}suchi.txt', 'r', encoding='utf-8') as f:
                p_suchi = f.read()
    else:
        pass

    return render_template('partner.html',
                           yourType=yourType[0:-2],
                           p_Type = p_Type,
                           p_suchi = p_suchi,
                           p_kekka = p_kekka,
                           picture = img_path,
                           p_picture = p_img_path)

if __name__ == '__main__':
    app.run()

