import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { AddRsvpService } from '../add-rsvp.service';
import { RSVP } from '../models/rsvp';
import { RsvpComponent } from '../rsvp/rsvp.component';
@Component({
  selector: 'app-rsvp-form',
  templateUrl: './rsvp-form.component.html',
  styleUrls: ['./rsvp-form.component.scss']
})
export class RsvpFormComponent implements OnInit {
  message: String;
  rsvpForm = new FormGroup({
    firstName: new FormControl(''),
    lastName: new FormControl(''),
    email: new FormControl(''),
    attending: new FormControl(''),
    numberAttending: new FormControl(''),
  });

  constructor(private rsvpService: AddRsvpService) {
      this.message = "";
   }

  ngOnInit(): void {
  }
  onSubmit() {
    this.rsvpService.postRSVP(this.rsvpForm.value as RSVP).subscribe((result)=>{
      console.log(result)
      this.message = "Successfully RSVPed! Thanks.";
    })
  }
}
