/*
 * This file handles reading the drones out of the MySqlDatabase and putting them into a List
 * @author Ionis Kutrolli
 */
using System;
using System.Collections.Generic;
using Database;
using MySql.Data.MySqlClient;
using UnityEngine;

namespace Drones
{
    public class CreateDrone
    {
        //Simple DataBase that handles the new drones added to MySql
        private MySqlDatabase creationDatabase = new MySqlDatabase("prep");

        //Connection for MySqlConnection to open a conenction with the Database
        private MySqlConnection _connection;

        //Reads the info from the MySqlDatabase
        private MySqlDataReader _reader;

        //Drone to be added to the list
        private Drone drone;

        //Keeps track of how many drones have been added to the field
        private int _uniqueNum = 0;

        //Unique identifier to find find the drones
        private String _uniqueID;

        //The list of drones 
        private List<Drone> drones = new List<Drone>();

        //The builder that makes an acceptable MySql connection string
        private MySqlConnectionStringBuilder _connectionString = new MySqlConnectionStringBuilder();

        //The command to pull info from MySql
        private MySqlCommand _command;

        private int droneCount = 0;

        // Start is called before the first frame update
        /// <summary>
        /// The function called at the start of the program to connect to the MySql database and create all the drones
        /// on the field
        /// </summary>
        public CreateDrone()
        {

        }

        public List<Drone> createList()
        {
            _connectionString.Server = "192.168.137.5";
            _connectionString.UserID = "Bois";
            _connectionString.Password = "HackUpstate";
            _connectionString.Database = "drones";
            _connection = new MySqlConnection(_connectionString.ToString());
            _connection.Open();
            _command = new MySqlCommand("SELECT id FROM drones", _connection);
            Debug.Log("Connection state:" + _connection.State);
            _reader = _command.ExecuteReader();
            while (_reader.Read())
            {
                drone = new Drone();
                drone.id = _reader["id"].ToString();
                drone.droneNum = _uniqueNum++;
                drones.Add(drone);
                droneCount++;
            }
            _connection.Close();
            _reader.Close();
            return drones;
        }

        public List<Drone> addNewDrones(List<Drone> drones, List<GameObject> objs)
        {
            _connectionString.Server = "192.168.137.5";
            _connectionString.UserID = "Bois";
            _connectionString.Password = "HackUpstate";
            _connectionString.Database = "drones";
            _connection = new MySqlConnection(_connectionString.ToString());
            _connection.Open();
            _command = new MySqlCommand("SELECT COUNT(id) FROM drones", _connection);
            var ids = Convert.ToInt32(_command.ExecuteScalar());
            var newDrones = new List<Drone>();
            while (droneCount < ids)
            {
                _command = new MySqlCommand("SELECT id FROM drones", _connection);
                _reader = _command.ExecuteReader();
                while (_reader.Read())
                {
                    if (!objs.Contains(GameObject.Find(_reader["id"].ToString())))
                    {
                        drone = new Drone();
                        drone.id = _reader["id"].ToString();
                        drone.droneNum = _uniqueNum++;
                        newDrones.Add(drone);
                    }
                }
                _reader.Close();
            }

            return newDrones;
        }
    }
}
