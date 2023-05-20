# ICT4D_g17

### How to access

Call +31203697664 with pin 597197.

### Components

- Server(app.py): our flask server. Serves vxml files, and fetch data from crop suggestion service and weather api.
- Weather api(Openweather): data source for weather data.
- Plant Suggestion service(Sqlite database): store crop suggestion based on weather and region.

### Suggestion schema

```sqlite
CREATE TABLE suggestion (weatherId int,
                         plantId int, 
                         suggest_en varchar(255), 
                         suggest_akan varchar(255), 
                         suggest_dagbani varchar(255)
                        )
```

#### Vxml 

- main.xml: entry of the app. Here user can select language and navigate to menu.
- menu.xml: User can select and weather data will be returned.
- weather_response.xml: Response for weather query. User can choose to get suggestion.
- suggestion_response.xml: Response for suggestion query.
