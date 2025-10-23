

### spim up local db 
## use commands: 
1. Swap into "postgres"-User: 
- sudo -i -u postgres
2. start postgres-console:
- psql 
3. Create new User defined in config.py:
- CREATE ROLE "erykMaushagen" WITH LOGIN SUPERUSER PASSWORT 'your-p-word';
4. leave postgresql: 
- \q
5. normal console: 
- exit

## create db: 
- CREATE DATABASE "erykdb" OWNER "erykMaushagen";


## access db: 
- psql -U erykMaushagen -d erykdb