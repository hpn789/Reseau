using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Cards : MonoBehaviour
{
    [SerializeField]
    Sprite[] _cardImgs;

    public Sprite GetImageById(int cardId)
    {
        return _cardImgs[cardId];
    }
}
