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
    ConnectToServer _connectionManager;

    [SerializeField]
    Cards _cardList;

    [SerializeField]
    Image[] _placeHolders;

    [SerializeField]
    GameObject[] _cards;

    [SerializeField]
    Image _lastCard;

    private int[] _cardIds = new int[9];
    private bool _playable = false;

    void Start()
    {
        /*_cardList.StartCards();
        int[] cards = new int[6];
        cards[0] = 111;
        cards[1] = 112;
        cards[2] = 111;
        cards[3] = 115;
        cards[4] = 114;
        cards[5] = 116;
        ShowDrawnCards(cards);*/
    }

    public void BeginTurn()
    {
        _playable = true;
    }

    public void ShowDrawnCards(string[] cardIds)
    {
        for(int i = 0; i < cardIds.Length && i<9; i++)
        {
            int id = int.Parse(cardIds[i]);
            if (id == -1)
                continue;
            _cards[i].SetActive(true);
            _placeHolders[i].sprite = _cardList.GetImageById(id);
            _cardIds[i] = id;
        }
    }

    public void HideAllCard()
    {
        for (int i = 0; i < _cards.Length; i++)
        {
            _cards[i].SetActive(false);
        }
    }

    public void ShowLastPlayed(int cardId, bool isVisible)
    {
        if (cardId == -1 || !isVisible)
            cardId = 81;
        _lastCard.sprite = _cardList.GetImageById(cardId);
    }

    public void PlayCard(int card)
    {
        if(_playable)
        {
            _cards[card].SetActive(false);
            //ShowLastPlayed(_cardIds[card]);
            _playable = false;
            string socket = "";
            _connectionManager.WriteSocket(socket);
        }
    }
}
