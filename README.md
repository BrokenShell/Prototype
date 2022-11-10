# Prototype Project
## Data Science Workshop

### Top Features
- Dynamic Data Pipeline
  - User Input => Database => User Output
- Interactive Analytics
  - User Input => Graph Output
- Predictive ML Model
  - User Input => Prediction Output

### Design Philosophy
- Readable
- Maintainable
- Extensible
- Declarative
- Polymorphic
- Encapsulated
- Abstractions

### Tech Stack
- Business Logic: Python
- Web Framework: Flask
- Database: MongoDB
- Graphs: Altair
- Machine Learning: Scikit
- Data Engineering: Pandas
- Template Engine: Jinja2
- Templates: HTML5
- Styles: CSS 3
- Client Scripting: JavaScript

### Build Local Docker Image
```shell
docker build . -t prototype
```

### Run Local Docker Image
```shell
docker run -it -p 8000:8000 prototype
```
