from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    context = {}
    context['rank1'] = 'Northrop Grumman/Boeing B-2 Spirit'
    context['rank2'] = 'Airbus A380'
    context['rank3'] = 'Lockheed Martin/Boeing F-22'
    context['rank4'] = 'Airbus A350'
    context['rank5'] = 'Boeing C-17 Globemaster'
    return render_template('index.html', context=context)

@app.route("/top1")
def top1():
    context = {}
    context['nome'] = 'Northrop Grumman/Boeing B-2 Spirit'
    context['valor'] = 'US$ 2,4 bilhões'
    context['titulo_da_pagina'] = 'O mais caro'
    context['link_imagem'] = 'https://upload.wikimedia.org/wikipedia/commons/1/10/B-2A_Spirit.jpg'

    return render_template('aviao.html', context=context)

@app.route("/top2")
def top2():
    context = {}
    context['nome'] = 'Airbus A380'
    context['valor'] = 'US$ 428 milhões'
    context['titulo_da_pagina'] = 'O segundo mais caro'
    context['link_imagem'] = 'https://www.melhoresdestinos.com.br/wp-content/uploads/2020/07/emirates-executiva-A380-capa.jpg'

    return render_template('aviao.html', context=context)

@app.route("/top3")
def top3():
    context = {}
    context['nome'] = 'Lockheed Martin/Boeing F-22'
    context['valor'] = 'US$ 350 milhões'
    context['titulo_da_pagina'] = 'O terceiro mais caro'
    context['link_imagem'] = 'https://3.bp.blogspot.com/-p4v2uTo2JlM/U40y29b_bEI/AAAAAAAAAJg/WfNoWXqFeLo/s1600/F-22+2180698.jpg'

    return render_template('aviao.html', context=context)

@app.route("/top4")
def top4():
    context = {}
    context['nome'] = 'Airbus A350'
    context['valor'] = 'US$ 341 milhões'
    context['titulo_da_pagina'] = 'O quarto mais caro'
    context['link_imagem'] = 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Qatar_Airways_A350-941_%28A7-ALA%29_landing_at_Frankfurt_Airport.jpg'

    return render_template('aviao.html', context=context)

@app.route("/top5")
def top5():
    context = {}
    context['nome'] = 'Boeing C-17 Globemaster'
    context['valor'] = 'US$ 328 milhões'
    context['titulo_da_pagina'] = 'O quinto mais caro'
    context['link_imagem'] = 'https://www.aeroin.net/wp-content/uploads/2021/03/1024px-C-17_4.jpg'

    return render_template('aviao.html', context=context)
