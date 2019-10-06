using MySql.Data.MySqlClient;
using UnityEngine;

namespace Drones
{
    public class drone_places : MonoBehaviour
    {
        private MySqlConnection _con = null;
        private MySqlCommand _cmd = null;
        private MySqlDataReader _rdr = null;
    
        private string connectionString = "localhost;Bois;HackUpstate";

        // Start is called before the first frame update
        void Start()
        {
            _con = new MySqlConnection(connectionString);
            _con.Open();
            Debug.Log("Connection state:" +_con.State);
        
            string cmd_string = "SELECT * FROM droneslocation";
            _cmd = new MySqlCommand(cmd_string, _con);
        
        }

        // Update is called once per frame
        void Update()
        {
            using (_rdr = _cmd.ExecuteReader())
            {
                while (_rdr.Read())
                {
                    Debug.Log(_rdr[0] + " -- " + _rdr[1]);
                }
            }
            {
            
            }
        }
    }
}
