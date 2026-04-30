.PHONY: setup evaluate test app

setup:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

evaluate:
	PYTHONPATH=src python -m meditation_ai.evaluate --config configs/evaluation.yaml

test:
	PYTHONPATH=src pytest -q

app:
	streamlit run app/streamlit_app.py
