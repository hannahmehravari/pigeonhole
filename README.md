# Pigeonhole

Pigeonhole lets you scrape emails of people present in a [Robin](https://robinpowered.com/) office by using the Robin API.

## How to run
Create an environment using the `requirements.txt` file.

Create a `.env` file in the root of the project and populate the following variable:
```
robin_api_base_url=
organisation_id=
```
Currently, the Robin API base URL is `https://api.robinpowered.com/v1.0/` and you can find the organisation ID in the admin setting in the Robin interface.

Run 
```
streamlit run app.py
```

You will need a Robin API access token to input into the app, which you can also generate through the admin settings in the Robin interface.
