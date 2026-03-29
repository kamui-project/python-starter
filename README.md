# Python Starter

A Flask sample application for [Kamui Platform](https://kamui-platform.com)

Please refer to the [documentation for Python app](https://docs.kamui-platform.com/gui/apps/python.html).

## Local Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python app.py
```

Open http://localhost:5000 in your browser.

## Deploy to Kamui Platform

### Dashboard Settings

| Setting | Value |
|---------|-------|
| Setup Command | *(leave empty)* |
| Pre-deploy Command | `alembic upgrade head` |
| Start Command | `gunicorn --config gunicorn.conf.py app:app` |
| Health Check Path | `/health` |

### Environment Variables

`PORT` is automatically set when you deploy app. <br>
`DATABASE_URL` is automatically set when you link a database to your app.

## Links

- [Kamui Platform](https://kamui-platform.com/)
- [Documentation](https://docs.kamui-platform.com/)
