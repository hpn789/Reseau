using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.Net;
using System.Net.Sockets;
using UnityEngine.UI;

public class CardsManager : MonoBehaviour
{
    [SerializeField]
    Cards _cardList;

    [SerializeField]
    Image[] _placeHolders;

    [SerializeField]
    GameObject[] _cards;

    [SerializeField]
    Image _lastCard;

    private int[] _cardIds;

    public void ShowDrawnCards(int[] cardIds)
    {
        for(int i = 0; i < cardIds.Length; i++)
        {
            _cards[i].SetActive(true);
            _placeHolders[i].sprite = _cardList.GetImageById(cardIds[i]);
            _cardIds[i] = cardIds[i];
        }
    }

    public void ShowLastPlayed(int cardId)
    {
        _lastCard.sprite = _cardList.GetImageById(cardId);
    }

    public void PlayCard(int card)
    {
        _cards[card].SetActive(false);
        ShowLastPlayed(_cardIds[card]);
    }
}
