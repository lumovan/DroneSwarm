using System;
using System.Collections.Generic;
using UnityEngine;

namespace Drones
{
    public class ManageDrones : MonoBehaviour
    {
        public GameObject Drone;
        private List<Drone> drones;
        private int numDrones = 0;
        private CreateDrone _createDrone;
        private DroneLocationUpdate _locationUpdate;
        private List<GameObject> _objects = new List<GameObject>();
        void Start()
        {
            QualitySettings.vSyncCount = 0;
            Application.targetFrameRate = 9999;
            _createDrone = new CreateDrone();
            drones = _createDrone.createList();
            numDrones = drones.Count;
            _locationUpdate = new DroneLocationUpdate(drones);
            _locationUpdate.UpdateLocation();
            drones = _locationUpdate.getDrones();
            foreach (var drone in drones)
            {
                GameObject _drone = Instantiate(Drone, drone.position, Quaternion.identity);
                _drone.name = drone.id; 
                _objects.Add(_drone);
                var name = _drone.AddComponent<Name>();
                name.name = drone.droneNum.ToString();
            }
        }

        public void Update()
        {
            _locationUpdate.UpdateLocation();
            drones = _locationUpdate.getDrones();
            foreach (var drone in drones)
            {
                var obj = GameObject.Find(drone.id);
                obj.transform.position = drone.position;
            }
            
            var tempDrones = _createDrone.addNewDrones(drones, _objects);
            if (tempDrones.Count != 0)
            {
                foreach (var drone in tempDrones)
                {
                    GameObject _drone = Instantiate(Drone, drone.position, Quaternion.identity);
                    _drone.name = drone.id; 
                    _objects.Add(_drone);
                    var name = _drone.AddComponent<Name>();
                    name.name = drone.droneNum.ToString();
                }
                drones.AddRange(tempDrones);
            }
        }
    }
}