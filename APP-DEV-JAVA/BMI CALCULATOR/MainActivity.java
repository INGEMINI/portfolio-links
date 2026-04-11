
package com.example.bmiapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

public class MainActivity extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    setContentView(R.layout.activity_main);

    TextView txtresult;
    LinearLayout llmain;
    EditText edtweight, edtheightft, edtheightin;
    Button btncalculate;

    edtweight = findViewById(R.id.edtweight);
    edtheightft = findViewById(R.id.edtheightft);
    edtheightin = findViewById(R.id.edtheightin);

    btncalculate = findViewById(R.id.btncalculate);
    txtresult = findViewById(R.id.txtresult);
    llmain = findViewById(R.id.llmain);
    btncalculate.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {

        int wt = Integer.parseInt(edtweight.getText().toString());
        int ft = Integer.parseInt(edtheightft.getText().toString());
        int in = Integer.parseInt(edtheightin.getText().toString());
        int totalin = ft * 12 + in;

        double totalcm = totalin * 2.53;
        double totalm = totalcm / 100;
        double bmi = wt / (totalm * totalm);
        if (bmi > 25) {
          txtresult.setText("you r over weight");
          llmain.setBackgroundColor(ContextCompat.getColor(MainActivity.this, R.color.colorow));
        } else if (bmi < 18) {
          txtresult.setText("you r under weight");
          llmain.setBackgroundColor(ContextCompat.getColor(MainActivity.this, R.color.coloruw));
        } else {
          txtresult.setText("you r healthy");
          llmain.setBackgroundColor(ContextCompat.getColor(MainActivity.this, R.color.colorh));
        }

      }
    });

  }
}