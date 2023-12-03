import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PredictionComponent } from './prediction/prediction.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'predict', component: PredictionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
