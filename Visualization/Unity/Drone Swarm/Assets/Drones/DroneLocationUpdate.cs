using System;
using System.Collections.Generic;
using Database;
using MySql.Data.MySqlClient;
using UnityEngine;


namespace Drones
{ 
    public class DroneLocationUpdate
    {
        //Simple DataBase that handles the new drones added to MySql
        private MySqlDatabase creationDatabase = new MySqlDatabase("prep");

        //Connection for MySqlConnection to open a conenction with the Database
        private MySqlConnection _connection;

        //Reads the info from the MySqlDatabase
        private MySqlDataReader _reader;
        
        //The builder that makes an acceptable MySql connection string
        private MySqlConnectionStringBuilder _connectionString = new MySqlConnectionStringBuilder();

        //The command to pull info from MySql
        private MySqlCommand _command;

        private List<Drone> drones;
        

        public DroneLocationUpdate(List<Drone> drones)
       {
           this.drones = drones;
       }
       

       public void addtoDroneList(Drone drone)
        {
            drones.Add(drone);
        }

        public void  UpdateLocation()
        {
            _connectionString.Server = "192.168.137.5";
            _connectionString.UserID = "Bois";
            _connectionString.Password = "HackUpstate";
            _connectionString.Database = "drones";
            _connection = new MySqlConnection(_connectionString.ToString());
            _connection.Open();
            foreach (var drone in drones)
            {
                // SELECT locx, locy, locz from droneslocation where id=
//                _command = locationDatabase.makeCommand("SELECT", "locX, locY, locZ, dirX, dirY, dirZ",
//                    "droneslocation", drone.id);
                _command = new MySqlCommand(String.Format("SELECT locX, locY, locZ, dirX, dirY, dirZ FROM droneslocation WHERE id={0}","\""+ drone.id + "\""), _connection);
                _reader = _command.ExecuteReader();
                while (_reader.Read())
                {
                    drone.position = new Vector3(Convert.ToSingle(_reader["locX"]),
                        Convert.ToInt32(_reader["locY"]),
                        Convert.ToInt32(_reader["locZ"]));
                    drone.velocity = new Vector3(Convert.ToSingle(_reader["dirX"]),
                        Convert.ToInt32(_reader["dirY"]),
                        Convert.ToInt32(_reader["dirZ"]));
                }
                _reader.Close();
            }
            
            _connection.Close();
        }

        public List<Drone> getDrones()
        {
            return drones;
        }
    }
}