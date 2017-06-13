using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Train : MonoBehaviour {

    [SerializeField]
    Place[] places;

    public void unactiveAllCharacter()
    {
        for(int i =0; i<places.Length;i++)
        {
            places[i].unactiveAllCharacters();
        }
    }

    public Place getPlace(int nb)
    {
        return places[nb];
    }
    
    // Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
