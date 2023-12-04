import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PredictionComponent } from './prediction/prediction.component';
import { SinglepredictionComponent } from './singleprediction/singleprediction.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'predict', component: PredictionComponent },
  { path: 'predict/1', component: SinglepredictionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
