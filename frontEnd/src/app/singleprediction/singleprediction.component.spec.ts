import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SinglepredictionComponent } from './singleprediction.component';

describe('SinglepredictionComponent', () => {
  let component: SinglepredictionComponent;
  let fixture: ComponentFixture<SinglepredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SinglepredictionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SinglepredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
