import { TestBed } from '@angular/core/testing';

import { AddRsvpService } from './add-rsvp.service';

describe('AddRsvpService', () => {
  let service: AddRsvpService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AddRsvpService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
