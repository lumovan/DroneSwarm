using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Configuration;
using System.Data;

using MySql.Data;
using MySql.Data.MySqlClient;

public class drone_places : MonoBehaviour
{
    private MySqlConnection con = null;
    private MySqlCommand cmd = null;
    private MySqlDataReader rdr = null;
    
    private string connectionString = "localhost;Bois;HackUpstate";

    // Start is called before the first frame update
    void Start()
    {
        con = new MySqlConnection(connectionString);
        con.Open();
        string cmd_string = "SELECT * FROM droneslocation";
        cmd = new MySqlCommand(cmd_string);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
