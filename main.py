from sanic import Sanic, response
import spacy

app = Sanic(__name__)
nlp = spacy.load('en')


@app.route('/', methods=['POST','GET'])
async def test(request):
    doc = nlp('{}'.format(request.body))
    resp = {'entities': []}
    print(doc.ents)
    for ent in doc.ents:
        ent_data = dict(text=ent.text, type=ent.label_, start=ent.start_char, end=ent.end_char)
        resp['entities'].append(ent_data)
    return response.json(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)