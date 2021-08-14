import { Component, OnDestroy, OnInit } from '@angular/core';
import { AddRsvpService } from '../add-rsvp.service';

@Component({
  selector: 'app-rsvp',
  templateUrl: './rsvp.component.html',
  styleUrls: ['./rsvp.component.scss'],
})
export class RsvpComponent implements OnInit {

  constructor(private rsvpService: AddRsvpService) {
  }

  ngOnInit(): void {
  }

}
