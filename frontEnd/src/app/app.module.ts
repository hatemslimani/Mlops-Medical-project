import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { CardioComponent } from './cardio/cardio.component';
import { PredictionComponent } from './prediction/prediction.component';
import { SinglepredictionComponent } from './singleprediction/singleprediction.component';

@NgModule({
  declarations: [AppComponent, HomeComponent, CardioComponent, PredictionComponent, SinglepredictionComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
