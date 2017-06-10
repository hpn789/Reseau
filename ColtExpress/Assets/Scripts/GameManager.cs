using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    [SerializeField]
    GameObject _panel;

    [SerializeField]
    Text[] _scores;

    public void EndGame(int[] scores)
    {
        _panel.SetActive(true);
        for(int i = 0; i < _scores.Length; i++)
        {
            _scores[i].text = scores[i].ToString();
        }
    }
}
