using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class CharacterManager : MonoBehaviour
{
    [SerializeField]
    Train train;

    [SerializeField]
    Player[] players;

    [SerializeField]
    Image[] playerPortrait;

    [SerializeField]
    Sprite[] characterPortrait;

    [SerializeField]
    CardsManager cardManager;

    [SerializeField]
    GameObject waitingPlayers;

    [SerializeField]
    GameObject scoreCanvas;

    [SerializeField]
    Text[] scores;

    [SerializeField]
    GameObject[] choices;

    public void updateGameState(string gameState)
    {
        char sep1 = '|';
        char sep2 = '~';
        char sep3 = ' ';

        string[] infos = gameState.Split(sep1);

        train.unactiveAllCharacter();
        
        //maj info joueur buton + position
        for(int i=1;i<5 && i<infos.Length;i++)
        {
            string[] infosJoueur = infos[i].Split(sep2);
            players[i - 1].setNbBourses(infosJoueur[2]);
            players[i - 1].setNbcase("0");
            players[i - 1].setNbDiamonds(infosJoueur[3]);
            players[i - 1].setNbBalles(int.Parse(infosJoueur[0]));
            train.getPlace(int.Parse(infosJoueur[1])).activateCharacter(i - 1);
        }

        //maj position marshall
        train.getPlace(int.Parse(infos[8])).activateCharacter(4);

        //maj butin train
        string[] infosTrain = infos[6].Split(sep3);
        for(int i=0;i<infosTrain.Length;i++)
        {
            string[] infoWagon = infosTrain[i].Split(sep2);
            train.getPlace(i).setNbcase("0");
            train.getPlace(i).setNbBourses(infoWagon[0]);
            train.getPlace(i).setNbDiamonds(infoWagon[1]);
        }

        //maj place case
        int positionCase = int.Parse(infos[7]);
        if (positionCase < 10)
            train.getPlace(positionCase).setNbcase("1");
        else
            players[positionCase - 10].setNbcase("1");

        //récupère infos de tour
        int tour = int.Parse(infos[0]);

        //maj cartes joueur
        string[] cards = infos[5].Split(sep2);
        cardManager.HideAllCard();
        cardManager.ShowDrawnCards(cards);

        //maj état du jeu
        int state = int.Parse(infos[10]);
        switch(state)
        {
            case 0:
                string[] charac = infos[11].Split(sep3);
                for (int i = 0; i < 4; i++)
                {
                    playerPortrait[i].sprite = characterPortrait[int.Parse(charac[i])];
                }
                waitingPlayers.SetActive(true);
                break;
            case 3:
                for (int i = 0; i < choices.Length; i++)
                {
                    choices[i].SetActive(true);
                }
                break;
            case 4:
                string[] playerScores = infos[11].Split(sep3);
                for (int i = 0; i < 4; i++)
                {
                    scores[i].text = playerScores[i].ToString();
                }
                scoreCanvas.SetActive(true);
                break;
            default:
                if (waitingPlayers.activeSelf)
                    waitingPlayers.SetActive(false);
                break;
        }

        //maj dernière carte pile
        string[] infosPile = infos[9].Split(sep2);
        int lastCard = int.Parse(infosPile[0]);
        bool isCardVisible = int.Parse(infosPile[1]) == 1 ? true : false;

        cardManager.ShowLastPlayed(lastCard, isCardVisible);
    } 
}
