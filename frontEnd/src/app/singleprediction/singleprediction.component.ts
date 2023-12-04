import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-singleprediction',
  templateUrl: './singleprediction.component.html',
  styleUrls: ['./singleprediction.component.scss'],
})
export class SinglepredictionComponent implements OnInit {
  constructor(private route: ActivatedRoute) {}
  prediction;
  ngOnInit(): void {
    this.prediction = JSON.parse(this.route.snapshot.paramMap.get('data'));
    console.log(this.prediction);
  }
}
