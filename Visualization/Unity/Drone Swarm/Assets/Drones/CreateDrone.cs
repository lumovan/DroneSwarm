using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using MySql.Data.MySqlClient;
using UnityEditor.Build.Reporting;
using UnityEngine;

namespace Drones
{
    public class CreateDrone : MonoBehaviour
    {
        public GameObject Drone;
        private Vector3 location = new Vector3(0,0,0);
        private MySqlConnection _connection = null;
        private MySqlDataReader _reader;
        private Drone drone = new Drone();
        private int _uniqueNum = -1;
        private List<Drone> drones = new List<Drone>();
        private MySqlConnectionStringBuilder _connectionString = new MySqlConnectionStringBuilder();
        private MySqlCommand _command;
        // Start is called before the first frame update
        void Start()
        {
            _connectionString.Server = "192.168.137.5";
            _connectionString.UserID = "Bois";
            _connectionString.Password = "HackUpstate";
            _connectionString.Database = "prep";
            _connection = new MySqlConnection(_connectionString.ToString());
            _connection.Open();
            Debug.Log("Connection state:" + _connection.State);
            _command = new MySqlCommand("SELECT id FROM drones", _connection);
            ;
            _reader = _command.ExecuteReader();
            while (_reader.Read())
            {
                Debug.Log("Hello");
                drone.id = _reader.ToString();
                drone.droneNum = _uniqueNum++;

                Instantiate(Drone, new Vector3(location.x++, location.y, location.z), Quaternion.identity);
                Drone.name = drone.droneNum.ToString();

            }
        }

        // Update is called once per frame
        void Update()
        {
        
        }
    }
}
