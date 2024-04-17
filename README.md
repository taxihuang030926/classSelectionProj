# classSelectionProj

This is a midterm project from FCU DBMS Course of a 3-tier application of a course selection system for a mocked up university CCU.

## Usage
Please install Python3.10 or above

```
// only for unix users

./env_crt.sh
```

Once the procedure is done
Please first create a yaml file `config.yml`
```
database:
  host: "0.0.0.0"
  port: "3306"
  user: <any_user_name>
  password: "<any_password>"
  database: classselectionproj
```

1. Open XAMPP, startup Apache and MySQL Server
2. Open up [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
3. Create `classselectionproj` and setup a user
4. Import SQL files in `db` directory into `classselectionproj`
5. Start up Flask run, default run at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```
python main.py
```