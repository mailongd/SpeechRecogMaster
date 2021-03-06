package com.example.speechrecognition;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
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
    TextView tv;
    EditText et;
    Button button;

    boolean word = false;
    private int contentView;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_mic, container, false);
    }

    @SuppressLint("CutPasteId")
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        setContentView(R.layout.fragment_mic);

        mTextTv = (TextView) getView().findViewById(R.id.textTv);
        mTextResponses = (TextView) getView().findViewById(R.id.textTv);
        mVoiceBtn = (ImageButton) getView().findViewById(R.id.voiceBtn);
        wordBank = Arrays.asList(getResources().getStringArray(R.array.Words));
        responses = Arrays.asList(getResources().getStringArray(R.array.responses));

        et = getView().findViewById(R.id.phone);
        tv = getView().findViewById(R.id.text_view);
        button = getView().findViewById(R.id.button);

        if (!Python.isStarted())
            Python.start(new AndroidPlatform(getActivity()));

        Python py = Python.getInstance();
        final PyObject pyf = py.getModule("Test"); // python file

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String getPlainText = et.getText().toString();
                // analyse mood here
                PyObject analyseMood = pyf.callAttr("returnMood", getPlainText); // python func
                String returnMood = analyseMood.toString();
                tv.setText(returnMood);
            }

        });

        //create array list and connect it to xml file
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

    public void setContentView(int contentView) {
        this.contentView = contentView;
    }
    public int getContentView() {
        return contentView;
    }
}

