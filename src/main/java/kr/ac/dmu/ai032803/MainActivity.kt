package kr.ac.dmu.ai032803

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kr.ac.dmu.ai032803.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_main)
        var vb = ActivityMainBinding.inflate(layoutInflater)
        setContentView(vb.root)

    }
}