import { Component, OnInit } from '@angular/core';
// import { ActivatedRoute } from '@angular/router';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-prediction',
  templateUrl: './prediction.component.html',
  styleUrls: ['./prediction.component.scss'],
})
export class PredictionComponent implements OnInit {
  constructor(private route: ActivatedRoute) {}
  prediction;
  predictionArray: any[];
  ngOnInit(): void {
    const predictionObject = JSON.parse(
      this.route.snapshot.paramMap.get('data')
    );
    this.predictionArray = Object.keys(predictionObject).map(
      (key) => predictionObject[key]
    );
    this.prediction = JSON.parse(this.route.snapshot.paramMap.get('data'));
  }
}
