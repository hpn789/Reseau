using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System;
using System.IO;
using System.Net.Sockets;

public class ConnectToServer : MonoBehaviour
{
    [SerializeField]
    string IP = "127.0.0.1";

    [SerializeField]
    int port = 1337;
    
    bool _socketReady = false;
    TcpClient _socket;
    NetworkStream _stream;
    StreamWriter _writer;
    StreamReader _reader;

    void Start ()
    {
        try
        {
            _socket = new TcpClient(IP, port);
            _stream = _socket.GetStream();
            _writer = new StreamWriter(_stream);
            _reader = new StreamReader(_stream);
            _socketReady = true;
            _stream.ReadTimeout = 1;
        }
        catch (Exception e)
        {
            Debug.Log("Socket error: " + e);
        }
    }

    void Update()
    {
        if (!_socketReady || !_stream.DataAvailable)
        {
            return;
        }
        try
        {
            Debug.Log(_reader.ReadLine());
        }
        catch (Exception e)
        {
            Debug.Log("Socket error: " + e);
            return;
        }
    }

    public void WriteSocket(string line)
    {
        if (!_socketReady)
        {
            return;
        }
        _writer.WriteLine(line + Environment.NewLine);
        _writer.Flush();
    }

    public void CloseSocket()
    {
        if (!_socketReady)
        {
            return;
        }
        _writer.Close();
        _reader.Close();
        _socket.Close();
        _socketReady = false;
    }
}
