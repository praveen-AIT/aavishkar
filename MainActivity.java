package com.example.geek.aavishkar_final;


import android.content.pm.PackageManager;
import android.location.Location;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationServices;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity implements GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener {

    private TextView myLocationText;
    private GoogleApiClient googleApiClient;

    private static final String THINGSPEAK_API_KEY = "YHP7FBKEX11LTXS0";

    /* Be sure to use the correct fields for your own app*/
    private static final String THINGSPEAK_FIELD1 = "field1";
    private static final String THINGSPEAK_FIELD2 = "field2";

    private static final String THINGSPEAK_UPDATE_URL = "https://api.thingspeak.com/update?api_key=YHP7FBKEX11LTXS0&";


    private WebView webview;

    public void initWebView(double latitude, double longitude)
    {
        webview= (WebView)findViewById(R.id.webview);
        webview.getSettings().setJavaScriptEnabled(true);
        webview.setWebViewClient(new WebViewClient());
        webview.loadUrl(THINGSPEAK_UPDATE_URL + THINGSPEAK_FIELD1 + "=" + latitude +
                "&" + THINGSPEAK_FIELD2 + "=" + longitude);
    }

    public void initViews()
    {
        myLocationText = (TextView) findViewById(R.id.myLocationText);

        GoogleApiClient.Builder builder = new GoogleApiClient.Builder(this);

        builder.addConnectionCallbacks(this);
        builder.addOnConnectionFailedListener(this);
        builder.addApi(LocationServices.API);

        googleApiClient = builder.build();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();

        final Handler handler = new Handler();

        final Runnable update = new Runnable() {

            public void run() {
                googleApiClient.connect(); // now onConnected will be called
            }
        };


        new Timer().schedule(new TimerTask() {

            @Override
            public void run() {
                handler.post(update);
            }
        }, 500, 7000);

    }


    @Override
    public void onConnected(Bundle bundle) {

        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {

            Toast.makeText(this, "Grand The permissions", Toast.LENGTH_SHORT).show();
        }
        else {
            Location location = LocationServices.FusedLocationApi.getLastLocation(googleApiClient); // its the last known location

            double latitude = location.getLatitude();
            double longitude = location.getLongitude();

            myLocationText.setText(String.format("Location %s,%s", latitude, longitude));

            initWebView(latitude, longitude);

        }

    }




    @Override
    public void onConnectionSuspended(int i) {

    }

    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {

    }
}