using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class CharacterManager : MonoBehaviour
{
    [SerializeField]
    Sprite[] _characters;

    [SerializeField]
    GameObject[] _placeHoldersGO;

    [SerializeField]
    Text[] _charactersTreasures;

    [SerializeField]
    Text[] _wagonsTreasures;

    Image[] _placeHoldersImg = new Image[40];
    GameObject[] _activatedPlaces = new GameObject[5];
    Dictionary<int, int> _placeNumber = new Dictionary<int, int>();

    void Start()
    {
        for(int i = 0; i < 10; i++)
        {
            _placeNumber.Add(i, 0);
        }

        int activated = 0;
        for(int i = 0; i < _placeHoldersGO.Length; i++)
        {
            _placeHoldersImg[i] = _placeHoldersGO[i].GetComponent<Image>();
            if(_placeHoldersGO[i].activeInHierarchy)
            {
                _activatedPlaces[activated++] = _placeHoldersGO[i];
            }
        }
    }

    public void PlaceCharacters(Dictionary<int, int> places)
    {
        for(int i = 0; i < _activatedPlaces.Length; i++)
        {
            _activatedPlaces[i].SetActive(false);
        }

        for (int i = 0; i < 10; i++)
        {
            _placeNumber[i] = 0;
        }

        int activated = 0;
        for (int i = 0; i < places.Count; i++)
        {
            _placeHoldersGO[4 * places[i] + _placeNumber[places[i]]].SetActive(true);
            _activatedPlaces[activated++] = _placeHoldersGO[4 * places[i] + _placeNumber[places[i]]];
            _placeHoldersImg[4 * places[i] + _placeNumber[places[i]]].sprite = _characters[i];
            _placeNumber[places[i]]++;
        }
    }

    public void GiveTreasuresToPlayers(Dictionary<int, int> treasures)
    {
        for(int i = 0; i < treasures.Count; i++)
        {
            _charactersTreasures[i].text = treasures[i].ToString();
        }
    }

    public void PlaceTreasuresInWagons(Dictionary<int, int> treasures)
    {
        for (int i = 0; i < treasures.Count; i++)
        {
            _wagonsTreasures[i].text = treasures[i].ToString();
        }
    }
}
