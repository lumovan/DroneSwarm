using System;
using MySql.Data.MySqlClient;

namespace Database
{
    public class MySqlDatabase
    {
        public String IP_ADDR = "192.168.137.5";
        public String USER_ID = "Bois";
        public String PWD = "HackUpstate";
        
        private MySqlConnection _connection;
        private MySqlConnectionStringBuilder _connectionString = new MySqlConnectionStringBuilder();

        public MySqlDatabase(String database)
        {
            
            _connectionString.Server = IP_ADDR;
            _connectionString.UserID = USER_ID;
            _connectionString.Password = PWD;
            _connectionString.Database = database;
        }

        public MySqlConnection getConnection()
        {
            return new MySqlConnection(_connectionString.ToString());
        }

        public MySqlCommand makeCommand(String keyword, String column, String table)
        {
            return  new MySqlCommand(keyword + " " + column + " FROM " + table, getConnection());
        }
        public MySqlCommand makeCommand(String keyword, String column, String table, String id)
        {
            return  new MySqlCommand(keyword + " " + column + " FROM " + table + "WHERE id= " + id , getConnection());
        }
    }
}