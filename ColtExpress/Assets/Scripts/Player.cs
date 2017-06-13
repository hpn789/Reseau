using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Player : MonoBehaviour {

    [SerializeField]
    Text nbBourses;

    [SerializeField]
    Text nbDiamonds;

    [SerializeField]
    Text nbCases;

    private int nbBalles;

    int position;

    public void setNbBalles(int nb)
    {
        nbBalles = nb;
    }

    public int getNbBalles()
    {
        return nbBalles;
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

    public void setPosition(int p)
    {
        position = p;
    }

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
