# Fastapi-mysql

Demonstrate fastapi and mysql. 

## Installation

Install mysql (and optionally mysql workbench), create a database instance

Install dependencies

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Configure database url.
```bash
mv .env.template .env
```

Edit .env file and set your mysql instance url 

```bash
URL_DATABASE='mysql+pymysql://root:password@localhost:3306/database-schema'
```

## Usage

To run the server
```bash
uvicorn main:app --reload
```

To access swagger docs navigate to 

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)