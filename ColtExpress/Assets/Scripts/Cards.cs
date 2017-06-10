using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Cards : MonoBehaviour
{
    [SerializeField]
    Sprite[] _cardImgs;

    [SerializeField]
    int[] _cardIds;

    private Dictionary<int, Sprite> _cards = new Dictionary<int, Sprite>();

    public void StartCards()
    {
        for(int i = 0; i < _cardIds.Length; i++)
        {
            _cards.Add(_cardIds[i], _cardImgs[i]);
        }
    }

    public Sprite GetImageById(int cardId)
    {
        return _cards[cardId];
    }
}
