# Decompound

Utility for trying to find possible compound-combination for a german word using an own dictionary.

- Uses stemming for dictionary and scanning through word
- Finds all possible combinations

# Example

```python
> from decompound import decompound
> dictionary = ['Haus', 'besichtigung', 'vereinbarung']
> decompound('Häuserbesichtigungsvereinbarungen', dictionary)
[['Häuser', 'besichtigungs', 'vereinbarungen']]
```
