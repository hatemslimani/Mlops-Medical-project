import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root',
})
export class ConnexionService {
  private uri: String = 'http://20.56.18.178:8000/';
  // private uri: String = 'http://backend:8000/';
  constructor(private http: HttpClient) {}
  getPred(log) {
    return this.http.post(this.uri + 'predict', log);
  }
  getPredByCsv(data) {
    return this.http.post(this.uri + 'predict/csv', data);
  }
}
