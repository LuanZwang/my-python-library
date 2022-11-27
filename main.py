from flask import Flask, request
import json
from .service.basicService import BasicService

main = Flask(__name__)

service = BasicService()

class App:
    @main.route("/api/authors", methods=['GET', 'POST'])
    def authors():
        if request.method == 'GET':
            data = service.get_something(request.args.get("id"))
            
            json_docs = []
            for doc in data:
                json_doc = json.dumps(doc)
                json_docs.append(json_doc)

            print(data)
            print(json_docs)

            return {
            'data': json_docs,
            'method': request.method
            }

        if request.method == 'POST':
            result = service.insert_something(request.json)

            result_id = json.dumps(result, default=str)

            return {
                'id': result_id,
                'method': request.method,
		        'body': request.json
            }

from .controller import authorController

if __name__ == "__main__":
    main.run(host="0.0.0.0", port=8000, debug=True)
