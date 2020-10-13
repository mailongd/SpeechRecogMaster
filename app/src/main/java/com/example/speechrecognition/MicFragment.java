package com.example.speechrecognition;

import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

import static android.app.Activity.RESULT_OK;


public class MicFragment extends Fragment {

    private static final int REQUEST_CODE_SPEECH_INPUT = 1000;
    //views from activity
    TextView mTextTv;
    TextView mTextResponses;
    ImageButton mVoiceBtn;
    List<String> wordBank = new ArrayList<>();
    List<String> responses = new ArrayList<>();
    boolean word = false;
    View view;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_mic, container, false);
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        mTextTv = (TextView) getView().findViewById(R.id.textTv);
        mTextResponses = (TextView) getView().findViewById(R.id.textTv);
        mVoiceBtn = (ImageButton) getView().findViewById(R.id.voiceBtn);
        wordBank = Arrays.asList(getResources().getStringArray(R.array.Words));
        responses = Arrays.asList(getResources().getStringArray(R.array.responses));

        //button click to show speech to text dialog
        mVoiceBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                speak();
            }
        });
    }

    public void speak() {
        //intent to show speech to text dialog
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Hi say something");
        startActivityForResult(intent, REQUEST_CODE_SPEECH_INPUT);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        super.onActivityResult(requestCode, resultCode, intent);

        //this is the counter for the responses loop
        int responseItem = 0;
        if (requestCode == REQUEST_CODE_SPEECH_INPUT && resultCode == RESULT_OK) {
            ArrayList<String> result = intent.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
            mTextTv.setText(result.get(0).toUpperCase());
            //loops every word in a phrase until it keyword from wordBank
            for (String wordItem : wordBank) {
                if (result.get(0).contains(wordItem)) {
                    mTextResponses.setText(responses.get(responseItem).toString());
                    break;
                }
                //item +1
                //this moves to the next word, and it will check if there is key word in word item
                responseItem++;
            }
        }
    }
}

