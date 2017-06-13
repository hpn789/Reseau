using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Place : MonoBehaviour {

    [SerializeField]
    Text nbBourses;

    [SerializeField]
    Text nbDiamonds;

    [SerializeField]
    Text nbCases;

    [SerializeField]
    GameObject[] characters;

    public void activateCharacter(int nb)
    {
        characters[nb].SetActive(true);
    }

    public void unactiveAllCharacters()
    {
        foreach(GameObject go in characters)
        {
            go.SetActive(false);
        }
    }

    public void setNbcase(string s)
    {
        nbCases.text = s;
    }

    public void setNbDiamonds(string s)
    {
        nbDiamonds.text = s;
    }

    public void setNbBourses(string s)
    {
        nbBourses.text = s;
    }

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
