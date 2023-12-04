import {
  AfterViewInit,
  Component,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { ConnexionService } from './connexion.service';
declare var $: any;
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'frontEnd';
  @ViewChild('pre') form: NgForm;
  selectedFile: File | null = null;
  constructor(private conService: ConnexionService, private router: Router) {}

  ngOnInit(): void {}
  getPred(value) {
    this.conService.getPred(value).subscribe((data: any) => {
      (<any>$('#exampleModal2')).modal('hide');
      this.router.navigate(['/predict/1', { data: JSON.stringify(data) }]);
    });
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onSubmit() {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('file', this.selectedFile);
      this.conService.getPredByCsv(formData).subscribe((data) => {
        (<any>$('#exampleModal')).modal('hide');
        console.log(data);
        this.router.navigate(['/predict', { data: JSON.stringify(data) }]);
      });
    }
  }
}
