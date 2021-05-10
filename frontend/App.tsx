import React, { useEffect, useState } from 'react';
import { Label } from 'Styles';
import { SUBSCRIPTION_TYPE } from 'SubscriptionType';

export const App = () => {
  const [subscriptions, setSubscriptions] = useState([]);
  const [subscriptionSubmitResults, setSubscriptionSubmitResults] = useState<any>({});
  const read = async () => {
    const request = await fetch('http://localhost:8000/read/');
    const results = await request.json();
    setSubscriptions(results);
  }
  const create: React.FormEventHandler<HTMLFormElement> = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    const formData = new FormData(e.target as HTMLFormElement);
    const request = await fetch('http://localhost:8000/create', {
      method: 'POST',
      body: formData,
    });
    const results = await request.json();
    setSubscriptionSubmitResults(results);
    read();
  }
  useEffect(() => {
    read();
  }, [])
  return <div>
    <h2>Subscriptions</h2>
    <h2>Create New Subscription</h2>
    <form onSubmit={create}>
      <Label>
        Name{' '} 
        <input name='name'/>
      </Label>
      <Label>
        Email{' '}
        <input name='email'/> <strong>{subscriptionSubmitResults.error?.email_address}</strong>
      </Label>
      <Label>
        Subscription Type{' '}
        <select name='subscription'>
          {Object.keys(SUBSCRIPTION_TYPE).map((subscriptionTypeKey) => (
            <option key={subscriptionTypeKey} value={subscriptionTypeKey}>
              {SUBSCRIPTION_TYPE[subscriptionTypeKey]}
            </option>
          ))}
        </select>
      </Label>
      <button>Create</button>
      {subscriptionSubmitResults.success === true && 'Successfully added a subscription'}
      {subscriptionSubmitResults.success === false && 'Failed to add a subscription'}
    </form>
    {subscriptions.map((subscription, subscriptionIndex) => (
      <div key={subscriptionIndex}>
        <div>{subscriptionIndex + 1}</div>
        <div>{subscription.fields.name}</div>
        <div>{subscription.fields.email_address}</div>
        <div>{SUBSCRIPTION_TYPE[subscription.fields.subscription_type]}</div>
      </div>
    ))}
  </div>
}