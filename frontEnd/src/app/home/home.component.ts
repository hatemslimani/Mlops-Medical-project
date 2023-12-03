import {
  AfterViewInit,
  Component,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { NgForm } from '@angular/forms';
import { ConnexionService } from '../connexion.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  @ViewChild('pre') form: NgForm;
  selectedFile: File | null = null;
  constructor(private conService: ConnexionService, private router: Router) {}

  ngOnInit(): void {}
  getPred(value) {
    this.conService.getPred(value).subscribe((data: any) => {
      this.router.navigate(['/predict', { data: JSON.stringify(data) }]);
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
        console.log(data);
      });
    }
  }
}
