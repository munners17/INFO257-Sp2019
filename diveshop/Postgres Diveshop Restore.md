## Postgres Load and List Tables Insructions

### createdb [documentation](https://www.postgresql.org/docs/11/app-createdb.html)
`createdb diveshop`

### Restoring the dump [documentation](https://www.postgresql.org/docs/11/backup-dump.html#BACKUP-DUMP-RESTORE)
`psql --set ON_ERROR_STOP=on diveshop < diveshopdump_pg.sql`

### Since database is loaded to the diveshop schema, use this command to access tables
`\dt diveshop.`
